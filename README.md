# FastAPI Practice

Python / FastAPI 기본 기능 연습용 프로젝트입니다.

## 실행 환경

Python 3.11 이상 권장

Python 버전 확인

```powershell id="0gagk7"
python --version
```

## 가상환경

프로젝트 루트에서 가상환경 생성

```powershell id="rlc58q"
python -m venv .venv
```

PowerShell

```powershell id="4u2cgo"
.\.venv\Scripts\Activate.ps1
```

CMD

```cmd id="80cc78"
.venv\Scripts\activate.bat
```

## 패키지 설치

```powershell id="x8f8ft"
pip install -r requirements.txt
```

## 실행

```powershell id="ud25qk"
uvicorn app.main:app --env-file ./app/.env --reload
```

또는

```powershell id="49ak25"
python -m uvicorn app.main:app --reload
```

## 확인

서버 실행 후 아래 주소에서 확인할 수 있습니다.

```text id="0nfh6g"
http://127.0.0.1:8000
http://127.0.0.1:8000/docs
```

`/docs`에서 Swagger UI를 통해 API를 테스트할 수 있습니다.

## 기본 문법

```python id="dnbr8g"
app = FastAPI()
```

FastAPI 애플리케이션 생성

```python id="0rxoxm"
@app.get("/users")
```

GET API 등록

```python id="pzz3l1"
def get_user(user_id: int):
```

함수 선언 및 타입 지정

```python id="ht84iu"
class UserCommand(BaseModel):
```

Request Body 데이터 정의

```python id="t5f6gi"
return {"status": "OK"}
```

dict 반환 시 JSON 형태로 응답
