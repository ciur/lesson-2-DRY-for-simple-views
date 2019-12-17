from django.shortcuts import render


def about(request):

    return render(
        request, 'demoapp/about.html',
    )


def privacy_policy(request):

    return render(
        request, 'demoapp/privacy_policy.html',
    )


def cookies_policy(request):

    return render(
        request, 'demoapp/cookies_policy.html',
    )


def terms(request):

    return render(
        request, 'demoapp/terms.html',
    )
