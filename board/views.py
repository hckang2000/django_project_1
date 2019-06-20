from django.shortcuts import render, redirect
from django.http import Http404
from .models import Board
from .forms import BoardForm
from fcuser.models import Fcuser
from django.core.paginator import Paginator
from tag.models import Tag

# Create your views here.

def board_list(request):
    all_boards = Board.objects.all().order_by('-id')
    page = int(request.GET.get('p',1)) # 전체 페이지를 p 라는 변수로 받을꺼고, 없으면 1로 가져옴 
    paginator = Paginator(all_boards,2) # 한페이지에 2개씩 보여줄 것
    boards = paginator.get_page(page)
    return render(request, 'board_list.html', {'boards': boards})

def board_write(request):
    if not request.session.get('user'):
        return redirect('/fcuser/login/')
    if request.method =="POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk = user_id)

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser 
            board.save()

            tags = form.cleaned_data['tags'].split(',') #board 모델을 생성해서 id 가 생성되어야 함. 
            for tag in tags:
                if not tag:
                    continue
                _tag, created = Tag.objects.get_or_create (name=tag) #조건에 해당하는게 있으면 가져오고, 아니면 만들어준다. 생성된 클래스변수와 생성된 것인지의 여부를 반환해줌.
                board.tags.add(_tag)


            return redirect('/board/list/')
    else:
        form = BoardForm()
    return render(request, 'board_write.html', {'form': form})

def board_detail (request, pk):
    try:
        board = Board.objects.get(pk = pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다.')
    
    return render(request, 'board_detail.html', {'board': board}) 
