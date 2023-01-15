from django.shortcuts import render

# Create your views here.


def example_view(request):
    
    return render(request, 'my_app/example.html')


def variable_view(request):
    my_var = {
        'first_name':'Stoyan',
        'last_name':'Trendafilov',
        'some_list':[1,2,3,4,4],
        'some_dict':{'inside_key':'value_key'}
    }
    return render(request, 'my_app/variable.html', context=my_var)