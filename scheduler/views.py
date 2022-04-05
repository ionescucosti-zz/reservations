from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from scheduler.models import Rental, Reservations


def index(request):
    result = []
    rentals = [rental['name'] for rental in Rental.objects.all().values()]
    for i in range(len(rentals)):
        reservations = Reservations.objects.filter(rental=rentals[i]).values()
        for j in range(len(reservations)):
            if j > 0:
                result.append([
                        reservations[j]['rental_id'],
                        f"Res-{reservations[j]['id']}",
                        reservations[j]['checkin'],
                        reservations[j]['checkout'],
                        'Res-' + str(reservations[j - 1]['id'])
                    ])
            else:
                result.append([
                        reservations[j]['rental_id'],
                        f"Res-{reservations[j]['id']}",
                        reservations[j]['checkin'],
                        reservations[j]['checkout'],
                        '-'
                    ])
    return render(request, "index.html", {'entries': result},)


class reservations(APIView):
    def get(self, request):
        result = []
        rentals = [rental['name'] for rental in Rental.objects.all().values()]
        for i in range(len(rentals)):
            reservations = Reservations.objects.filter(rental=rentals[i]).values()
            for j in range(len(reservations)):
                if j > 0:
                    result.append({
                            'Rental_name': reservations[j]['rental_id'],
                            'ID': f"Res-{reservations[j]['id']}",
                            'Checkin': reservations[j]['checkin'],
                            'Checkout': reservations[j]['checkout'],
                            'previous_id': 'Res-' + str(reservations[j - 1]['id'])
                        })
                else:
                    result.append({
                            'Rental_name': reservations[j]['rental_id'],
                            'ID': f"Res-{reservations[j]['id']}",
                            'Checkin': reservations[j]['checkin'],
                            'Checkout': reservations[j]['checkout'],
                            'previous_id': '-'
                        })
        return Response(result, status=status.HTTP_200_OK)
