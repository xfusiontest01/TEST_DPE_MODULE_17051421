from datetime import datetime
from airflow import DAG
from airflow.providers.microsoft.azure.transfers.azure_blob_to_gcs import AzureBlobStorageToGCSOperator

with DAG(dag_id="TEST_DPE_MODULE",schedule_interval="0 * * * *",start_date=datetime(2021,11,22),concurrency=16,max_active_runs=16,dagrun_timeout=None,orientation="LR",catchup=True,is_paused_upon_creation=False) as dag:

    a = AzureBlobStorageToGCSOperator(wasb_conn_id="wasb_default",gcp_conn_id="google_cloud_default",blob_name="a",file_path="a",container_name="a",bucket_name="a",object_name="a",filename="a",gzip=False,delegate_to="a",task_id="a",email_on_retry=False,email_on_failure=False,retries=0,retry_exponential_backoff=False,depends_on_past=False,wait_for_downstream=False,priority_weight=1,pool_slots=1,task_concurrency=None,do_xcom_push=True)

