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


# ... (imports remain unchanged)
class ChatbotAPIView(APIView):
    def post(self, request, *args, **kwargs):
        prompt = request.data.get('prompt')
        title = request.data.get('title') 
        all_conversations = Conversation.objects.all()
        
        if all_conversations:
            all_conversations_conversations = "\n".join([f"User: {c.prompt}\nAI: {c.response}" for c in all_conversations])
            print(all_conversations_conversations)
        else :
            all_conversations = ' '
        if prompt or title:
            cache_key = title

            # Use redis_client.lrange to get the list of conversation data from Redis
            cache_data = redis_client.lrange(cache_key, 0, -1)

            # Decode the bytes and load each JSON string
            decoded_cache_data = [json.loads(data.decode('utf-8')) for data in cache_data]

            if decoded_cache_data:
                # Update the logic for accessing the list of conversations
                previous_conversations = "\n".join([f"User: {c['prompt']}\nAI: {c['response']}" for c in decoded_cache_data])
                prompt_with_previous  = all_conversations_conversations + f"{previous_conversations}\nUser: {prompt}\nAI:"
                print(previous_conversations)
            else:
                prompt_with_previous = f"User: {prompt}\nAI:"
            print(prompt_with_previous)
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
            conversation = {"prompt": prompt, "title": title, "response": response}
            
            # Serialize the conversation dictionary to JSON before storing in Redis
            serialized_conversation = json.dumps(conversation)

            # Update the cache lpush logic to append the serialized conversation to the list
            redis_client.lpush(cache_key, serialized_conversation)

            # Serializer를 통해 JSON 응답 생성
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




