from django import forms

class PlayerSearchForm(forms.Form):
    player1 = forms.CharField(label='Player 1', max_length=100)
    player2 = forms.CharField(label='Player 2', max_length=100)