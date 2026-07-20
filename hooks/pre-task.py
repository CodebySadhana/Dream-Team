from datetime import datetime
REQUIRED=["task_id","objective","owner","priority","department"]
def run(task):
    missing=[k for k in REQUIRED if not task.get(k)]
    if missing: raise ValueError(f"Missing: {missing}")
    task["validated_at"]=datetime.utcnow().isoformat()
    return {"allow_execution":True,"task":task}
