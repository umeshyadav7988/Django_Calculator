from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def calculate(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            num1 = float(data.get("num1"))
            num2 = float(data.get("num2"))
            operation = data.get("operation")

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 == 0:
                    return JsonResponse({"error": "Cannot divide by zero"}, status=400)
                result = num1 / num2
            else:
                return JsonResponse({"error": "Invalid operation"}, status=400)

            return JsonResponse({"result": result})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)
