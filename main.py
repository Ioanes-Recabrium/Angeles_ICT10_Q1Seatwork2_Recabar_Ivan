from pyscript import document
def compute(event):
    num1 = float(document.querySelector("#num1").value)
    num2 = float(document.querySelector("#num2").value)
    operation = document.querySelector("#operation").value
    if operation == "+":
        answer = num1+num2
    elif operation == "-":
        answer = num1-num2
    elif operation == "x":
            answer = num1*num2
    elif operation == "/":
        if num2 == 0:
            document.querySelector("#result").innerText="We can't really divide by 0"
            return
        answer = num1/num2
    document.querySelector("#result").innerText="YOUR RESULT IS..." + str(answer)