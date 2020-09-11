# -*- coding: utf-8 -*-
# @Author: shubhambansal
# @Date:   2018-02-04 22:43:58
# @Last Modified by:   shubhambansal
# @Last Modified time: 2018-02-04 22:57:32
from rest_framework import serializers
from .models import Shop


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
