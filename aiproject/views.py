from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from formapp.models import NewModel
from django.shortcuts import render
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def home(request):
    # return(HttpResponse('<h1>Welcome to BTP</h1>'))
    return render(request,'home.html')

def forestmodel(request):
    # return(HttpResponse('<h1>Welcome to BTP</h1>'))
    return render(request,'forestmodel.html')

def allcharts(request):
    # Retrieve data from the database
    queryset = NewModel.objects.all()

    # Initialize an empty list to store base64-encoded images
    graphics = []

    # Iterate over the columns
    for i in range(1, 21):  # Assuming you want to plot three columns (q1, q2, q3)
        # Retrieve data for the current column
        column_data = [obj.__getattribute__(f'q{i}') for obj in queryset]

        # Generate a plot for the current column
        plt.plot(column_data)
        plt.xlabel('X-axis label')
        plt.ylabel('Y-axis label')
        plt.title(f'Chart {i}: Line Plot')

        # Save the chart to a BytesIO object
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        # Encode the image to base64
        graphic = base64.b64encode(image_png)
        graphic = graphic.decode('utf-8')

        # Append the base64-encoded image to the list
        graphics.append(graphic)

        # Clear the current plot to prepare for the next iteration
        plt.clf()

    # Pass the list of base64-encoded images to the template
    context = {'graphics': graphics}

    return render(request,'allcharts.html',context)

# return(HttpResponse('<h1>Welcome to BTP</h1>'))
# return render(request,'allcharts.html')
def team(request):
    # return(HttpResponse('<h1>Welcome to BTP</h1>'))
    return render(request,'team.html')

def about(request):
    # return(HttpResponse('<h1>Welcome to BTP</h1>'))
    return render(request,'about.html')
def ouradmin(request):
    # return(HttpResponse('<h1>Welcome to Form</h1>'))
    return render(request, 'ouradmin.html')

def LogRegr(request):
    # return(HttpResponse('<h1>Welcome to Form</h1>'))
    return render(request, 'LogRegr.html')

def Hclustering(request):
    # return(HttpResponse('<h1>Welcome to Form</h1>'))
    return render(request, 'Hclustering.html')

# def login():
#     # return(HttpResponse('<h1>Welcome to Form</h1>'))
#     queryset = MyModel.objects.all()
#
#     column1_data = [obj.q1 for obj in queryset]
#     # column2_data = [obj.q2 for obj in queryset]
#
#     plt.plot(column1_data)
#     plt.xlabel('X-axis label')
#     plt.ylabel('Y-axis label')
#     plt.title('Chart 1: Line Plot')
#     chart1_file_path = 'charts/chart1.png'  # File path to save Chart 1
#     plt.savefig(chart1_file_path)
#     plt.clf()
#
#     context = {
#         'chart1_file_path': chart1_file_path,
#     }
#
#     return context



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username=="eeshir" and password=="12345":
            context=login()
            return render(request, 'login.html',context)
        else:
            return render(request, 'ouradmin.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'ouradmin.html')


# def home(request):
#     # return(HttpResponse('<h1>Welcome to PetVerse</h1>'))
#     return render(request,'webhome.html')
# views.py


def login():
    # Retrieve data from the database
    queryset = NewModel.objects.all().values('q1','q2','q3','q4','q5')
    data = pd.DataFrame(list(queryset))

    X = data[['q1','q2','q3','q4']]
    y = data['q5']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions on the testing set
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    coefficients = model.coef_
    print("Mean Squared Error:", mse)
    print("R-squared:", r2)

    graphics=[]

    # Generate a plot for the current column
    plt.scatter(y_test, y_test, color='red', label='Actual Values')
    plt.scatter(y_test, y_pred, color='green', label='Predicted Values')
    plt.xlabel("Actual Values")
    plt.ylabel("Predicted Values")
    plt.title("Actual vs Predicted Values")

    # Save the chart to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Encode the image to base64
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    # Append the base64-encoded image to the list
    graphics.append(graphic)

    # Clear the current plot to prepare for the next iteration
    plt.clf()

    features = ['q1','q2','q3','q4']
    plt.bar(features, model.coef_)
    plt.xlabel("Features")
    plt.ylabel("Coefficients")
    plt.title("Coefficients of Features")

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Encode the image to base64
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    # Append the base64-encoded image to the list
    graphics.append(graphic)

    # Clear the current plot to prepare for the next iteration
    plt.clf()

    residuals = y_test - y_pred
    plt.scatter(y_pred, residuals)
    plt.xlabel("Predicted Values")
    plt.ylabel("Residuals")
    plt.title("Residual Plot")
    plt.axhline(y=0, color='r', linestyle='-')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Encode the image to base64
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    # Append the base64-encoded image to the list
    graphics.append(graphic)

    # Clear the current plot to prepare for the next iteration
    plt.clf()

    # Pass the list of base64-encoded images to the template
    context = {'graphics': graphics,"mse": mse,"r2": r2,"coefficients":coefficients}

    return context

