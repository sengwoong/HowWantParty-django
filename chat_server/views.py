from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dotenv import load_dotenv
import openai
import os
import redis
from rest_framework.viewsets import ModelViewSet
from .models import Conversation
from .serializers import ConversationSerializer


import json

redis_client = redis.StrictRedis(host='localhost', port=6379, db=1)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

class ChatbotAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # 쿼리 매개변수에서 cache_key를 받아옴
        cache_key = request.query_params.get('cache_key', 'default_cache_key')

        # Redis에서 대화 데이터 목록 가져오기
        cache_data = redis_client.lrange(cache_key, 0, -1)

        # Bytes를 디코딩하고 각 JSON 문자열을 로드
        decoded_cache_data = [json.loads(data.decode('utf-8')) for data in cache_data]

        if decoded_cache_data:
            # 이전 대화 목록에 대한 로직 업데이트
            conversation_list = [
                {"User": c['prompt'], "Ai": c['response']} for c in decoded_cache_data
            ]
        else:
            conversation_list = [{"Error": "값이 없음"}]

        return Response({'conversation_list': conversation_list}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # POST 요청으로부터 데이터 가져오기
        prompt = request.data.get('prompt')
        title = request.data.get('title') 

        # 모든 대화 가져오기
        all_conversations = Conversation.objects.all()
        
        if all_conversations:
            # 모든 대화를 문자열로 포맷팅
            all_conversations_conversations = "\n".join([f"User: {c.prompt}\nAI: {c.response}" for c in all_conversations])
        else:
            all_conversations_conversations = ' '

        if prompt or title:
            cache_key = title

            # Redis에서 대화 데이터 목록 가져오기
            cache_data = redis_client.lrange(cache_key, 0, -1)

            # Bytes를 디코딩하고 각 JSON 문자열을 로드
            decoded_cache_data = [json.loads(data.decode('utf-8')) for data in cache_data]

            if decoded_cache_data:
                # 이전 대화 목록에 대한 로직 업데이트
                previous_conversations = "\n".join([f"User: {c['prompt']}\nAI: {c['response']}" for c in decoded_cache_data])
                prompt_with_previous = f"{all_conversations_conversations}\n이전 대화 목록:\n{previous_conversations}\nUser: {prompt}\nAI:"
            else:
                prompt_with_previous = f"User: {prompt}\nAI:"
            
            # OpenAI 모델을 사용하여 응답 생성
            # model_engine = "text-davinci-003"
            # completions = openai.Completion.create(
            #     engine=model_engine,
            #     prompt=prompt_with_previous,
            #     max_tokens=1024,
            #     n=5,
            #     stop=None,
            #     temperature=0.5,
            # )
            # response = completions.choices[0].text.strip()
            response = "결과"

            # 대화 정보를 딕셔너리로 저장
            conversation = {"prompt": prompt, "title": title, "response": response}
            
            # 대화 딕셔너리를 JSON으로 직렬화하여 Redis에 저장
            serialized_conversation = json.dumps(conversation)
            redis_client.lpush(cache_key, serialized_conversation)

            # 대화 정보를 JSON 응답으로 반환
            serializer = ConversationSerializer(conversation)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'error': 'No prompt provided'}, status=status.HTTP_400_BAD_REQUEST)



from rest_framework import viewsets


class MessageViewSet(viewsets.ModelViewSet):
    queryset =  Conversation.objects.all()
    serializer_class = ConversationSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)




