from datetime import datetime
def run(task,result):
    return {"status":"completed","completed_at":datetime.utcnow().isoformat(),"task":task,"result":result}
