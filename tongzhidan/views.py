from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView,\
    DetailView, DeleteView, UpdateView, TemplateView

from django.urls import reverse_lazy

from .models import Fachekehu, Daozhan, Guige, Huowu, Baozhuang, Fache, Jisuan
# from .forms import FacheForm, JisuanForm, Facheformset
from .forms import Facheformset, FacheForm


def index(request):
    fcs = Fache.objects.all()
    return render(request, 'index.html', locals())




def create(request):
    if request.method == 'POST':
        form_fc = FacheForm(request.POST)
        if form_fc.is_valid():
            fc = form_fc.save() #首先提交父表单
            form_fache = Facheformset(request.POST, instance=fc)
            #创建子表单,实例选择父表单
            if form_fache.is_valid():
                form_fache.save()  #提交子表单

        return redirect('/list/') #跳转首页
    else:
        form_fc = FacheForm()
        form_fache = Facheformset()

    return render(request, 'create_update.html', locals())



class FacheDelete(DeleteView):
    model = Fache
    success_url = reverse_lazy('list')


# def delete(request, pk):
#     fc = get_object_or_404(Fache, id=pk)
#     fc.delete()
#     return redirect('/list/')

def update(request, pk):
    fc = get_object_or_404(Fache, pk=pk)#查询实例
    if request.method == 'POST':
        form_fc = FacheForm(request.POST, instance=fc)#用实例和数据填充父表单
        if form_fc.is_valid():
            fc = form_fc.save()#提交父表单
            # 用实例和提交的数据填充子表单
            form_fache = Facheformset(request.POST, instance=fc)
            if form_fache.is_valid():
                form_fache.save()#提交子表单
        return redirect('/list/')
    else:
        form_fc = FacheForm(instance=fc)#用实例填充表单
        form_fache = Facheformset(instance=fc)#用实例填充表单
    return render(request, 'create_update.html', locals())




def detail(request, pk):
    fc = get_object_or_404(Fache, id=pk)
    jss = Jisuan.objects.filter(number=fc.id)

    sumjs, sumzl = [], []

    for js in jss:
        js.zhongliang = js.sum_zhongliang()
        sumjs.append(js.jianshu)
        sumzl.append(js.zhongliang)

    sumjianshu = sum(sumjs)
    sumzhongliang = sum(sumzl)

    return render(request, 'detail.html', locals())





# def model_create(request, modelform=None):
#     '''根据模型设置表单,本方法不如类视图.'''
#     if request.method == 'POST':
#         form = modelform(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/list/')
#     else:
#         form = modelform()
#
#     return render(request, 'model_create3.html', locals())








class About(TemplateView):
    template_name = 'about.html'





class HuowuList(ListView):
    model = Huowu
class HuowuDetail(DetailView):
    model = Huowu
class HuowuCreate(CreateView):
    model = Huowu
    success_url = reverse_lazy('huowu_list')
    fields = '__all__'
class HuowuUpdate(UpdateView):
    model = Huowu
    success_url = reverse_lazy('huowu_list')
    fields = '__all__'
class HuowuDelete(DeleteView):
    model = Huowu
    success_url = reverse_lazy('huowu_list')



class DaozhanList(ListView):
    model = Daozhan
class DaozhanDetail(DetailView):
    model = Daozhan
class DaozhanCreate(CreateView):
    model = Daozhan
    success_url = reverse_lazy('daozhan_list')
    fields = '__all__'
class DaozhanUpdate(UpdateView):
    model = Daozhan
    success_url = reverse_lazy('daozhan_list')
    fields = '__all__'
class DaozhanDelete(DeleteView):
    model = Daozhan
    success_url = reverse_lazy('daozhan_list')


class FachekehuList(ListView):
    model = Fachekehu
class FachekehuDetail(DetailView):
    model = Fachekehu
class FachekehuCreate(CreateView):
    model = Fachekehu
    success_url = reverse_lazy('fachekehu_list')
    fields = '__all__'
class FachekehuUpdate(UpdateView):
    model = Fachekehu
    success_url = reverse_lazy('fachekehu_list')
    fields = '__all__'
class FachekehuDelete(DeleteView):
    model = Fachekehu
    success_url = reverse_lazy('fachekehu_list')


class GuigeList(ListView):
    model = Guige
class GuigeDetail(DetailView):
    model = Guige
class GuigeCreate(CreateView):
    model = Guige
    success_url = reverse_lazy('guige_list')
    fields = '__all__'
class GuigeUpdate(UpdateView):
    model = Guige
    success_url = reverse_lazy('guige_list')
    fields = '__all__'
class GuigeDelete(DeleteView):
    model = Guige
    success_url = reverse_lazy('guige_list')


class BaozhuangList(ListView):
    model = Baozhuang
class BaozhuangDetail(DetailView):
    model = Baozhuang
class BaozhuangCreate(CreateView):
    model = Baozhuang
    success_url = reverse_lazy('baozhuang_list')
    fields = '__all__'
class BaozhuangUpdate(UpdateView):
    model = Baozhuang
    success_url = reverse_lazy('baozhuang_list')
    fields = '__all__'
class BaozhuangDelete(DeleteView):
    model = Baozhuang
    success_url = reverse_lazy('baozhuang_list')