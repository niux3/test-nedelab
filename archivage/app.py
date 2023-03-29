from fastapi import FastAPI, HTTPException, status, UploadFile
from fastapi.responses import FileResponse
import os

app = FastAPI()

@app.get("/file")
def download(path: str):
    if not (os.path.exists(path) and os.path.isfile(path)):
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Le fichier n'existe pas")
    return FileResponse(path)

"""
1. le poids du fichier
2. le type de fichier à déposer (image, txt, pdf, etc.) ==> on évite aussi le zip bomb.... 
3. le path où sera déposé le fichier
4. le nom du fichier
5. si le fichier est un binaire exécutable ! 

@app.put("/file")
def upload(path: str, tmp_file: UploadFile):
    with open(path, "wb") as f:
        f.write(tmp_file.file.read())
"""

@app.put("/file")
def upload(file: UploadFile):
    try:
        max_upload_file_size = 50000
        check = [
            os.access(file.filename, os.X_OK) == False,
            os.stat(file.filename).st_size < max_upload_file_size,
            file.filename.rsplit('.').pop() in ['png', 'gif', 'jpg', 'pdf', 'txt', 'jpeg']
        ]
        if not all(check):
            return {"message": f"le fichier envoyé doit être une image ou un pdf ou du texte. Il ne doit pas excéder plus de {max_upload_size / 1024}kio"}
        contents = file.file.read()
        with open(f"./destination/{file.filename}", "wb") as file_dest:
            file_dest.write(contents)
    except Exception:
        return {"message": "une erreur s'est produite lors du téléchargement du fichier"}
    finally:
        file.file.close()
    return {"message": f"téléchargement avec succès de : {file.filename}"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", port=8000, log_level="info")
