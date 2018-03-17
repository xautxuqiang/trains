from django import forms

class IndexForm(forms.Form):
    vertex_edge = forms.CharField(label="vertex and edge", help_text="Enter multiple sets of vertices, edges and weights, separated by commas. Input format, example:AB5, BC3, which means the weight of A to B is 5 and the weight of B to C is 3.")

class PathLengthForm(forms.Form):
    path = forms.CharField(label="path", help_text="Enter the path you want to go. Example: A-B-C, it means A to B to C.")

class ShortestPathForm(forms.Form):
    vertex_start = forms.CharField(label="vertex start", help_text="start vertex. Example: A")
    vertex_end = forms.CharField(label="vertex end", help_text="end vertex. Example: B")

class AllPathForm(forms.Form):
    vertex_start = forms.CharField(label="vertex start", help_text="start vertex. Example: A")
    vertex_end = forms.CharField(label="vertex end", help_text="end vertex. Example: B")
    times = forms.IntegerField(label="times")


class EqualTimesForm(forms.Form):
    vertex_start = forms.CharField(label="vertex start", help_text="start vertex. Example: A")
    vertex_end = forms.CharField(label="vertex end", help_text="end vertex. Example: B")
    times = forms.IntegerField(label="times")

class LessDistanceForm(forms.Form):
    vertex_start = forms.CharField(label="vertex start", help_text="start vertex. Example: A")
    vertex_end = forms.CharField(label="vertex end", help_text="end vertex. Example: B")
    distance = forms.IntegerField(label="distance")

