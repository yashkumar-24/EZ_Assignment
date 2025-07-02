from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from sqlalchemy.orm import Session
from app.auth.dependencies import get_current_user
from app.models.file import File as FileModel
from app.db import get_db
from app.utils.file_utils import save_upload_file

router = APIRouter()

@router.post("/login")
def ops_login():
    # TODO: Implement operation user login
    return {"msg": "Operation user login"}

@router.post("/upload", status_code=201)
def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db), user=Depends(get_current_user)):
    allowed_ext = [".pptx", ".docx", ".xlsx"]
    ext = file.filename[file.filename.rfind(""):] if "." in file.filename else ""
    if not any(file.filename.endswith(e) for e in allowed_ext):
        raise HTTPException(status_code=400, detail="Invalid file type")
    if not user.is_operation_user:
        raise HTTPException(status_code=403, detail="Not authorized")
    path = save_upload_file(file)
    db_file = FileModel(filename=file.filename, path=path, uploaded_by=user.id)
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return {"msg": f"File {file.filename} uploaded", "file_id": db_file.id} 