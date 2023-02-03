def get_time(time):
    h,m = time.split(":")
    return int(h)*60 + int(m)
def solution(book_time):
    rooms = []
    book_time.sort()
    for book in book_time:
        reserved = False
        for room in rooms:
            if get_time(room[-1][1]) + 10 <= get_time(book[0]):
                room.append(book)
                reserved = True
                break
        if not reserved:
            rooms.append([book])
    print(rooms)
    return len(rooms)