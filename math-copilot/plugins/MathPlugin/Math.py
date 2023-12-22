import math
import matplotlib.pyplot as plt
from semantic_kernel.skill_definition import (
    sk_function,
    sk_function_context_parameter,
)
from semantic_kernel.orchestration.sk_context import SKContext


class Math:
    @sk_function(
        description="Takes the square root of a number",
        name="Sqrt",
        input_description="The value to take the square root of",
    )
    def square_root(self, number: str) -> str:
        return str(math.sqrt(float(number)))

    @sk_function(
        description="Adds two numbers together",
        name="Add",
    )
    @sk_function_context_parameter(
        name="input",
        description="The first number to add",
    )
    @sk_function_context_parameter(
        name="number2",
        description="The second number to add",
    )
    def add(self, context: SKContext) -> str:
        return str(float(context["input"]) + float(context["number2"]))

    @sk_function(
        description="Subtract two numbers",
        name="Subtract",
    )
    @sk_function_context_parameter(
        name="input",
        description="The first number to subtract from",
    )
    @sk_function_context_parameter(
        name="number2",
        description="The second number to subtract away",
    )
    def subtract(self, context: SKContext) -> str:
        return str(float(context["input"]) - float(context["number2"]))

    @sk_function(
        description="Multiply two numbers. When increasing by a percentage, don't forget to add 1 to the percentage.",
        name="Multiply",
    )
    @sk_function_context_parameter(
        name="input",
        description="The first number to multiply",
    )
    @sk_function_context_parameter(
        name="number2",
        description="The second number to multiply",
    )
    def multiply(self, context: SKContext) -> str:
        return str(float(context["input"]) * float(context["number2"]))

    @sk_function(
        description="Divide two numbers",
        name="Divide",
    )
    @sk_function_context_parameter(
        name="input",
        description="The first number to divide from",
    )
    @sk_function_context_parameter(
        name="number2",
        description="The second number to divide by",
    )
    def divide(self, context: SKContext) -> str:
        return str(float(context["input"]) / float(context["number2"]))
    
    @sk_function(
        description="Calculate the sine of an angle in radians",
        name="Sine",
    )
    @sk_function_context_parameter(
        name="angle",
        description="The angle in radians",
    )
    def sine(self, context: SKContext) -> str:
        return str(math.sin(float(context["angle"])))

    @sk_function(
        description="Calculate the cosine of an angle in radians",
        name="Cosine",
    )
    @sk_function_context_parameter(
        name="angle",
        description="The angle in radians",
    )
    def cosine(self, context: SKContext) -> str:
        return str(math.cos(float(context["angle"])))

    @sk_function(
        description="Calculate the tangent of an angle in radians",
        name="Tangent",
    )
    @sk_function_context_parameter(
        name="angle",
        description="The angle in radians",
    )
    def tangent(self, context: SKContext) -> str:
        return str(math.tan(float(context["angle"])))

    @sk_function(
        description="Differentiate a function with respect to x",
        name="Differentiate",
    )
    @sk_function_context_parameter(
        name="expression",
        description="The mathematical expression to differentiate",
    )
    @sk_function_context_parameter(
        name="variable",
        description="The variable with respect to which to differentiate",
    )
    def differentiate(self, context: SKContext) -> str:
        # Basic implementation using sympy for symbolic differentiation
        from sympy import symbols, diff, simplify

        x = symbols(context["variable"])
        expression = context["expression"]
        derivative = diff(expression, x)
        simplified_derivative = simplify(derivative)
        return str(simplified_derivative)

    @sk_function(
        description="Integrate a function with respect to x",
        name="Integrate",
    )
    @sk_function_context_parameter(
        name="expression",
        description="The mathematical expression to integrate",
    )
    @sk_function_context_parameter(
        name="variable",
        description="The variable with respect to which to integrate",
    )
    def integrate(self, context: SKContext) -> str:
        # Basic implementation using sympy for symbolic integration
        from sympy import symbols, integrate, simplify

        x = symbols(context["variable"])
        expression = context["expression"]
        integral = integrate(expression, x)
        simplified_integral = simplify(integral)
        return str(simplified_integral)
    
    @sk_function(
        description="Plot a bar chart",
        name="BarChart",
    )
    @sk_function_context_parameter(
        name="categories",
        description="The categories for the bar chart",
    )
    @sk_function_context_parameter(
        name="values",
        description="The corresponding values for each category",
    )
    def bar_chart(self, context: SKContext) -> None:
        categories = context["categories"]
        values = context["values"]

        plt.bar(categories, values)
        plt.xlabel("Categories")
        plt.ylabel("Values")
        plt.title("Bar Chart")
        plt.show()

    @sk_function(
        description="Plot a pie chart",
        name="PieChart",
    )
    @sk_function_context_parameter(
        name="labels",
        description="The labels for each slice of the pie chart",
    )
    @sk_function_context_parameter(
        name="sizes",
        description="The sizes (proportions) for each slice",
    )
    def pie_chart(self, context: SKContext) -> None:
        labels = context["labels"]
        sizes = context["sizes"]

        plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
        plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title("Pie Chart")
        plt.show()