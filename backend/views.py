from django.shortcuts import render
from rest_framework import generics
from .serializers import CartSerializer,PictureSerializer
from .models import Cart,Picture,Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
import os,shutil
from django.conf import settings
from django.core.files.uploadedfile import TemporaryUploadedFile
from urllib.parse import unquote

class product_image:
    def __init__(self,title,url) -> None:
        self.title = title
        self.url = url

@api_view(['GET'])
def cart_api(request):
    filtered_products = Cart.objects.filter(mId = 1)
    querycart = filtered_products.select_related('pId','pId__picture')
    serializer = CartSerializer(querycart, many=True)

    return Response(serializer.data)


@api_view(['DELETE'])
def cart_delete(request,cart_id):
    try:
        cart_item = Cart.objects.get(pId=cart_id)
        cart_item.delete()
        return Response({"message": "Cart item deleted successfully."}, status=200)
    except Cart.DoesNotExist:
        return Response({"error": "Cart item is not found"}, status=404)
    
@api_view(['POST'])
@permission_classes([AllowAny])
def upload_product(request):
    if request.method == 'POST':
        form_data_json = request.data.get('page1')
        product_pic_files = request.FILES.getlist('product_pic')  # 使用 request.FILES 來獲取上傳的照片陣列
        auth_pic_files = request.FILES.getlist('auth_pic')
        print(form_data_json)
        print(product_pic_files)
        print(auth_pic_files)

        import json
        form_data = json.loads(form_data_json)
        products = Product(
            name=form_data['name'],
            brand=form_data['brand'],
            description=form_data['description'],
            age=form_data['age'],
            price = form_data['price'],
            size = form_data['length']+"*"+form_data['width']+"*"+form_data['height'] ,
            likes = 0,
            state = 'deposite',
            # 其他欄位根據需要添加
        )
        products.save()

        thispId = products.pId
        info_j = {
            "info": []
        }
        for file in product_pic_files:
            file_path = os.path.join(settings.MEDIA_ROOT, 'images', file.name)
            shutil.copyfile(file.temporary_file_path(), file_path)
            print(file.name)
            info_j["info"].append({
                "title": file.name,
                "url": "./media/images/" + file.name
            })
        info_json = json.dumps(info_j, ensure_ascii=False)

        print(info_j)
        product_pic_save_to_db = Picture.objects.create(
            pId = products,
            picture = info_json,
        )

        return JsonResponse({'message': '照片上傳成功！'})
    return JsonResponse({'message': '請使用 POST 請求上傳照片。'})


        

