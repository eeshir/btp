from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import NewForm



def success_url(request):
    return render(request, 'formapp/success.html')
    # return render(request, "formapp/form.html")

def my_form_view(request):
    print("Hello World")
    if request.method == 'POST':
        print("Hello")
        form = NewForm(request.POST)
        print(form)
        # print(form.q2)
        if form.is_valid():
            form_data = form.save(commit=False)  # Don't save to database yet
            form_data.q1 = request.POST.get('q1')
            form_data.q2 = request.POST.get('q2')
            form_data.q3 = request.POST.get('q3')
            form_data.q4 = request.POST.get('q4')
            form_data.q5 = request.POST.get('q5')
            form_data.q6 = request.POST.get('q6')
            form_data.q7 = request.POST.get('q7')
            form_data.q8 = request.POST.get('q8')
            form_data.q9 = request.POST.get('q9')
            form_data.q10 = request.POST.get('q10')
            form_data.q11 = request.POST.get('q11')
            form_data.q12 = request.POST.get('q12')
            form_data.q13 = request.POST.get('q13')
            form_data.q14 = request.POST.get('q14')
            form_data.q15 = request.POST.get('q15')
            form_data.q16 = request.POST.get('q16')
            form_data.q17 = request.POST.get('q17')
            form_data.q18 = request.POST.get('q18')
            form_data.q19 = request.POST.get('q19')
            form_data.q20 = request.POST.get('q20')
            form_data.save()

            return redirect('success_url')  # Redirect to a success URL
    else:
        form = NewForm()
    return render(request, 'formapp/form.html', {'form': form})

# Create your views here.