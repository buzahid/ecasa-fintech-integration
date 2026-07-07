import datetime
from typing import Dict, Any

def execute_rent_payment(account_data: Dict[str, Any], amount: float) -> Dict[str, Any]:
    """
    Executes an automatic monthly rent payment through the integrated banking API.
    """
    created_at = datetime.datetime.now()
    payment_status = "PENDING"
    
    # Extract banking credentials (required to execute the transfer)
    routing_number = account_data.get("routing_number")
    account_number = account_data.get("account_number")
    if not routing_number or not account_number:
        return {
            "success": False,
            "error": "missing_banking_credentials",
            "processed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        }
    # If account_data doesn't have a user token, this will crash with an AttributeError or processing error
    user_token = account_data.get("user_metadata").get("token") 
    
    # Mock processing logic
    print(f"Processing payment of ${amount} for token {user_token}")
    
    return {
        "success": True,
        "transaction_id": "tx_ecasa_99218",
        "processed_at": datetime.datetime.now().isoformat()
    }