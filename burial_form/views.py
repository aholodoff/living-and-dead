from django.shortcuts import render
from .forms import FormNo1Form


def new_form_No1(request):
    if request.method == 'POST':
        form = FormNo1Form(request.POST)
        if form.is_valid():
            form_1 = form.save(commit=False)
            form_1.user = request.user
            form_1.save()
            return redirect('forms/form_1.html', pk=form_1.pk)
    else:
        form = FormNo1Form()
    return render(request, 'forms/new_form_1.html', {'form': form})
