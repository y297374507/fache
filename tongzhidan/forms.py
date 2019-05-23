from django import forms
from .models import Fache, Jisuan, Daozhan, Huowu, Fachekehu, Guige, Baozhuang
from django.forms.models import inlineformset_factory




#利用内联表单创建父表单和子表单,设置子表单输入子段,显示数目
Facheformset = inlineformset_factory(Fache, Jisuan,
                                     fields=['guige','baozhuang', 'jianshu'],
                                     extra=6,
                                     can_delete=False)


class FacheForm(forms.ModelForm):
    class Meta:
        model = Fache
        # fields = ['date', 'daozhan', 'huowu',  'fachekehu']
        fields = '__all__'
        widgets = {
            'date': forms.SelectDateWidget(),
        }
#
#
# class JisuanForm(forms.ModelForm):
#     class Meta:
#         model = Jisuan
#         # fields = ['id', 'guige', 'baozhuang', 'jianshu']
#         exclude = ['number', ]


# class DaozhanForm(forms.ModelForm):
#     class Meta:
#         model = Daozhan
#         fields = '__all__'
#
# class HuowuForm(forms.ModelForm):
#     class Meta:
#         model = Huowu
#         fields = '__all__'
#
# class FachekehuForm(forms.ModelForm):
#     class Meta:
#         model = Fachekehu
#         fields = '__all__'
#
# class GuigeForm(forms.ModelForm):
#     class Meta:
#         model = Guige
#         fields = '__all__'
#
# class BaozhuangForm(forms.ModelForm):
#     class Meta:
#         model = Baozhuang
#         fields = '__all__'