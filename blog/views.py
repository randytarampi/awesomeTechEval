from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse

from dbe.blog.models import *

def main(request):
	# 2 items per page
	posts = Post.objects.all().order_by("-created")
	paginator = Paginator(posts, 2)
	# when no page is given, set page to 1
	try:
		page = int(request.GET.get("page", '1'))
	except ValueError: page = 1
	# we can have page numbers out of bounds so we need to check for that error
	try:
		posts = paginator.page(page)
	except (InvalidPage, EmptyPage):
		posts = paginator.page(paginator.num_pages)

	return render_to_response("list.html", dict(posts=posts, user=request.user))
