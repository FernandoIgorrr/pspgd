from django import forms

class FastaUploadForm(forms.Form):
    
    score_model_conservation = forms.ChoiceField(
        choices=[(1,'Aminoacid classification'),(2,'BLOSUM62')],
        widget=forms.RadioSelect(attrs={
            'class':'btn-check',
            'autocomplete':'off'
        }),
        required=True
    )
    
    xthreshold = forms.IntegerField(
        min_value   = 1,  
        initial     = 20,
        widget      = forms.NumberInput(attrs={
            'class': 'form-control ms-2',
            'style': 'width: 80px;height:30px'
        }),
        required    = True,
    )
    
    fasta_file  = forms.FileField(
        widget  = forms.ClearableFileInput(attrs={
            'class':'form-control',
            'style': 'width: 350px;'
        }),
        required=True
    )

    def clean_xthreshold(self):
        xthreshold = self.cleaned_data.get('xthreshold')
        if xthreshold < 1:
            raise forms.ValidationError("O valor mínimo para X-Threshold é 1.")
        return xthreshold