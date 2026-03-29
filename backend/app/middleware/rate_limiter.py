from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
import time
from collections import defaultdict


class RateLimiterMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, max_requests: int = 100, window_seconds: int = 60):
        super().__init__(app)
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.clients = defaultdict(list)

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        current_time = time.time()

        request_times = self.clients[client_ip]

        request_times = [
            t for t in request_times if current_time - t < self.window_seconds
        ]

        if len(request_times) >= self.max_requests:
            from fastapi.responses import JSONResponse

            return JSONResponse(
                status_code=429,
                content={"success": False, "error": "Too many requests"}
            )

        request_times.append(current_time)
        self.clients[client_ip] = request_times

        response = await call_next(request)
        return response
