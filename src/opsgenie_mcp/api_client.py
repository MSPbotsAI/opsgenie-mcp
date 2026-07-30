from typing import Any

import httpx


class OpsgenieError(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        super().__init__(f"Opsgenie API error {status_code}: {message}")


class OpsgenieClient:
    """Async httpx client wrapping the Opsgenie REST API.

    Auth is a static API key sent as `Authorization: GenieKey <apiKey>` — the
    same header format MSPbots' own integration uses.
    """

    def __init__(self, api_key: str, base_url: str):
        self._api_key = api_key
        self._base_url = base_url.rstrip("/")

    def _headers(self) -> dict[str, str]:
        return {
            "Authorization": f"GenieKey {self._api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def _clean_params(self, params: dict | None) -> dict:
        if not params:
            return {}
        return {k: v for k, v in params.items() if v is not None}

    async def get(self, path: str, params: dict | None = None) -> Any:
        return await self._request("GET", path, params=params)

    async def post(self, path: str, params: dict | None = None, json_body: Any = None) -> Any:
        return await self._request("POST", path, params=params, json_body=json_body)

    async def put(self, path: str, params: dict | None = None, json_body: Any = None) -> Any:
        return await self._request("PUT", path, params=params, json_body=json_body)

    async def patch(self, path: str, params: dict | None = None, json_body: Any = None) -> Any:
        return await self._request("PATCH", path, params=params, json_body=json_body)

    async def delete(self, path: str, params: dict | None = None) -> Any:
        return await self._request("DELETE", path, params=params)

    async def _request(
        self, method: str, path: str, params: dict | None = None, json_body: Any = None
    ) -> Any:
        async with httpx.AsyncClient(timeout=30.0) as client:
            try:
                resp = await client.request(
                    method,
                    f"{self._base_url}{path}",
                    headers=self._headers(),
                    params=self._clean_params(params),
                    json=json_body,
                )
            except httpx.RequestError as e:
                raise OpsgenieError(
                    0, f"{e or type(e).__name__} (url={self._base_url}{path})"
                ) from e
            self._raise_for_status(resp)
            return self._parse_body(resp)

    def _parse_body(self, resp: httpx.Response) -> Any:
        if not resp.content:
            return None
        try:
            return resp.json()
        except ValueError:
            return {"raw_response": resp.text}

    def _raise_for_status(self, resp: httpx.Response) -> None:
        if resp.status_code >= 400:
            try:
                detail = resp.json()
                if isinstance(detail, dict):
                    msg = detail.get("message") or str(detail)
                else:
                    msg = str(detail)
            except ValueError:
                msg = resp.text
            raise OpsgenieError(resp.status_code, str(msg))
