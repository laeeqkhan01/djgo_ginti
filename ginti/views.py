from django.shortcuts import render, get_object_or_404, redirect
from django.http      import HttpResponse
from .models          import AdadTable
from .forms           import AdadForm

# Create your views here.

def sab_aadaad(request):
  sabAdad = AdadTable.objects.all()
  return render(request, 'ginti/sab_aadaad.html', {'sabAdad': sabAdad})

def full_detail(request, pk):
  #tafseel = AdadTable.objects.get(pk=pk)
  tafseel = get_object_or_404(AdadTable, pk=pk)
  return render(request, 'ginti/full_detail.html', {'tafseel': tafseel})

def new_adad(request):
  if request.method == "POST":
    # Create a form instance from POST data
    rcvdForm = AdadForm(request.POST)
    if rcvdForm.is_valid():
      newEntry = rcvdForm.save(commit=False) # Get entry without saving
                                             # in the table, so it can be
                                             # edited
      newEntry.sqr = newEntry.num * newEntry.num
      newEntry.save()       # Now store entry in the DB 
      return redirect('full_detail', pk=newEntry.pk)
    else:
      return HttpResponse("------ received Form is invalid ---- 1 ---")
  else:
    form = AdadForm() # Create an empty form instance.
    return render(request, 'ginti/new_adad.html', {'form': form})

def edit_entry(request, pk):
  if request.method == "POST":
    # Get the object corresponding to row with this pk
    row = get_object_or_404(AdadTable, pk=pk)
    # Create a form with values from POST, corresp to above row
    form = AdadForm(request.POST, instance=row)
    if form.is_valid():
      # Get editable version of row object
      editable_row_obj = form.save(commit=False)
      editable_row_obj.sqr = editable_row_obj.num * editable_row_obj.num
      # Now, save object in the table
      editable_row_obj.save()
      # Now re-direct to full detail page for this row.
      return redirect('full_detail', pk=editable_row_obj.pk)
      # return HttpResponse('--------- Got form data ----1---')
  else:
    # Get the object corresponding to row with this pk
    row = get_object_or_404(AdadTable, pk=pk)
    # Create a form with values from the selected row
    form = AdadForm(instance = row)
    return render(request, 'ginti/new_adad.html', {'form': form})
    
