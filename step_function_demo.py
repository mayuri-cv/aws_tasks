x={
    "Comment": "A sample process step funcion",
    "StartAt": "ProcessTransaction",
    "States": {
        "ProcessTransaction": {
            "Type": "Choice",
            "Choices": [
                {
                    "Variable": "$.TransactionType",
                    "StringEquals": "PURCHASE",
                    "Next": "ProcessPurchase"
                },
                {
                    "Variable": "$.TransactionType",
                    "StringEquals": "REFUND",
                    "Next": "ProcessRefund"
                }
            ]

        },
        "ProcessRefund": {
            "Type": "Task",
            "Resource": "",
            "End": true
        },
        "ProcessPurchase": {
            "Type": "Task",
            "Resource": "",
            "End": true
        }
    }
}