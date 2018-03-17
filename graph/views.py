from django.shortcuts import render, redirect, reverse
from .forms import IndexForm, PathLengthForm, ShortestPathForm, AllPathForm, EqualTimesForm, LessDistanceForm
from django.http import HttpResponse

import json, os
import networkx as nx
import matplotlib.pyplot as plt

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = IndexForm(request.POST)
        if form.is_valid():
            data_input = form.cleaned_data['vertex_edge']
            # Generate graph.
            graph(data_input)
            return redirect(reverse("graph:graphDisplay"))
    else:
        form = IndexForm()
        context = {'form': form}
    return render(request, 'graph/index.html', context)

# global easy to use
g = {}

# AB5,BC4,CD8,DC8,DE6,AD5,CE2,EB3,AE7
def graph(data_input):
    data_input_list = data_input.split(',')
    # vertex set
    vertex = set()
    for d in data_input_list:
        # condition: key not in g
        if d[0] not in g:
            g[d[0]] = [(d[1:2], int(d[2:])),]
        else:
            g[d[0]].append((d[1:2], int(d[2:])))
        vertex.add(d[0])
        vertex.add(d[1:2])
    for v in vertex:
        g[v].append((v, 0))
    return g
    
def graph_display(request):
    print(g)
    vertexes = []
    edges = []
    # v: vertex, w: end_vertex and weight
    for v,w in g.items():
        vertexes.append(v)
        # add edges. (start_vertex, end_vertex, weight)
        for end, weight in w:
            edges.append((v, end, {'weight': weight}))
    # draw directed graph
    DG = nx.MultiDiGraph()
    DG.add_nodes_from(vertexes)
    DG.add_edges_from(edges)
    nx.draw_networkx(DG)
    # save the directed graph png
    plt.savefig('/home/xu/trains/graph/static/graph/direct-graph.png')
    context = {'graph': g}
    return render(request, 'graph/graphDisplay.html', context)

#################################################
def path_length(request):
    if not g:
        return redirect(reverse('graph:index'))
    form = PathLengthForm()
    if request.method == 'POST':
        form = PathLengthForm(request.POST)
        if form.is_valid():
            path = form.cleaned_data['path']
            # lengtg calc
            length = path_length_calc(path)
            return HttpResponse("This path' length is {}".format(length))
    context = {'form': form}
    return render(request, 'graph/pathLengthCalc.html', context)

# path length calculate function
def path_length_calc(path):
    path_list = path.split('-') # ['A','B','C']
    print(g)
    length = 0
    # calculate (vertexes -1)
    for i in range(len(path_list)-1):
        if path_list[i] in g:
            for edge_weight in g[path_list[i]]:
              if edge_weight[0] == path_list[i+1]:
                 length += edge_weight[1]
                 break
            # not find
            else:
                 length = "no path like this."
                 return length
        # vertex not in graph.
        else:
            legnth = "no path like this."
            return length
    return length

################################

def shortest_path(request):
    if not g:
        return redirect(reverse('graph:index'))
    form = ShortestPathForm()
    if request.method == 'POST':
         form = ShortestPathForm(request.POST)
         if form.is_valid():
             vertex_start = form.cleaned_data['vertex_start']
             vertex_end = form.cleaned_data['vertex_end']
             # calculate the shortest path result
             if vertex_end != vertex_start:
                 result = shortest_path_calc(vertex_start, vertex_end)
             else:
                 result = shortest_path_calc1(vertex_start)
             return HttpResponse("The {} to {} 's shortest path is {}".format(vertex_start, vertex_end, result))
    context = {'form': form}
    return render(request, 'graph/shortestPath.html', context)

# if vertex_start = vertex_end
def shortest_path_calc1(v_start):
    result = []
    for v_end in g:
        if v_end  == v_start: continue
        result1 = shortest_path_calc(v_start, v_end)
        result2 = shortest_path_calc(v_end, v_start)
        result.append(result1+result2)
    return min(result)

def shortest_path_calc(v_start, v_end):
    inf = float('inf') 
    #
    book = set()
    minv = v_start

    dis = dict((key, inf) for key in g.keys())
    dis[v_start] = 0

    for i in range(len(dis)):
        book.add(minv)
        # update distance
        for w in g[minv]:
            if dis[minv] + w[1] < dis[w[0]]:
                dis[w[0]] = dis[minv] + w[1]
        # update vertex
        new = inf
        for v in dis.keys():
            if v in book:
                continue
            if dis[v] < new:
                new = dis[v]
                minv = v
    return dis[v_end]
    
################################################33
def all_path(request):
    return render(request, 'graph/allPath.html')

######################################################
def less_times(request):
    if not g:
        return redirect(reverse('graph:index'))
    form = AllPathForm()
    if request.method == 'POST':
        form = AllPathForm(request.POST)
        if form.is_valid():
            v_start = form.cleaned_data['vertex_start']
            v_end = form.cleaned_data['vertex_end']
            times = form.cleaned_data['times']
            # storage the all path result
            global lesstimes_result_path
            lesstimes_result_path = []
            all_path_calc_lesstimes(v_end, [v_start], times)
            return HttpResponse('ALl path is {}'.format(lesstimes_result_path))
    context = {'form': form}
    return render(request, 'graph/lessTimes.html', context)


# condition <= time
def all_path_calc_lesstimes(v_end, path, times):
    if len(path)-1 > times:
        return
    # end is the v_end
    if len(path) > 1 and path[-1] == v_end:
        lesstimes_result_path.append(path)
    for w in g[path[-1]]:
        if w[1] == 0:
            continue
        all_path_calc_lesstimes(v_end, path+[w[0]], times)

#####################################################
def equal_times(request):
    if not g:
        return redirect(reverse('graph:index'))
    form = EqualTimesForm()
    if request.method == 'POST':
        form = EqualTimesForm(request.POST)
        if form.is_valid():
            v_start = form.cleaned_data['vertex_start']
            v_end = form.cleaned_data['vertex_end']
            times = form.cleaned_data['times']
            # result
            global equaltimes_result_path
            equaltimes_result_path = []
            all_path_calc_equaltimes(v_end, [v_start], times) 
            return HttpResponse('All Path is {}'.format(equaltimes_result_path))
    context = {'form': form}
    return render(request, 'graph/equalTimes.html', context)

# condition = time
def all_path_calc_equaltimes(v_end, path, times):
    if len(path)-1 > times:
        return
    # end is the v_end
    if len(path) == times+1 and path[-1] == v_end:
        equaltimes_result_path.append(path)
    for w in g[path[-1]]:
        if w[1] == 0:
            continue
        all_path_calc_equaltimes(v_end, path+[w[0]], times)


########################################################
def less_distance(request):
    if not g:
        return redirect(reverse('graph:index'))
    form = LessDistanceForm()
    if request.method == 'POST':
        form = LessDistanceForm(request.POST)
        if form.is_valid():
            v_start = form.cleaned_data['vertex_start']
            v_end = form.cleaned_data['vertex_end']
            distance = form.cleaned_data['distance']
            # result
            global lessdis_result_path
            lessdis_result_path = []
            all_path_calc_lessdistance(v_end, [v_start,], distance) 
            return HttpResponse('All Path is {}'.format(lessdis_result_path))
    context = {'form': form}
    return render(request, 'graph/lessDistance.html', context)


# condition less and equal distance
def all_path_calc_lessdistance(v_end, path, distance):
    if distance <= 0:
        return
    if len(path) >1 and v_end == path[-1]:
        lessdis_result_path.append(path)
    for w in g[path[-1]]:
        if w[1] == 0:
            continue
        all_path_calc_lessdistance(v_end, path+[w[0]], distance-w[1])

