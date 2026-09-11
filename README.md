# FastAPI Practice

PLC 제어 시스템을 가정한 아주 작은 FastAPI 연습 프로젝트입니다.

## 1. Python 확인

```powershell
python --version
```

Python 3.11 이상을 권장합니다.

## 2. 가상환경 생성

프로젝트 폴더에서:

```powershell
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

CMD:

```cmd
.venv\Scripts\activate.bat
```

## 3. 패키지 설치

```powershell
pip install -r requirements.txt
```

## 4. 서버 실행

```powershell
uvicorn app.main:app --reload
```

또는:

```powershell
python -m uvicorn app.main:app --reload
```

## 5. 확인

브라우저에서 아래 주소를 확인합니다.

- http://127.0.0.1:8000
- http://127.0.0.1:8000/plc/status
- http://127.0.0.1:8000/plc/1
- http://127.0.0.1:8000/docs  (Swagger UI)

## 코드에서 볼 문법

`app = FastAPI()` : FastAPI 애플리케이션 생성

`@app.get("/...")` : GET API 등록 (Decorator)

`@app.post("/...")` : POST API 등록

`def get_plc(device_id: int)` : Python 함수와 타입 힌트

`class PlcCommand(BaseModel)` : 요청 JSON을 받을 Pydantic 모델

`return { ... }` : dict를 반환하면 FastAPI가 JSON으로 변환

## POST 테스트

서버 실행 후 `/docs`에서 `POST /plc/command`를 선택하고 Try it out을 누른 뒤:

```json
{
  "device_id": 1,
  "running": true
}
```

을 보내보세요.
