from rest_framework import serializers

from svazi.models import Book, Author, Genre


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    genre = GenreSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        author = validated_data.pop('author')
        genre = validated_data.pop('genre')
        author_id, s = Author.objects.get_or_create(**author)
        book_id = Book.objects.create(author=author_id, **validated_data)
        for i in genre:
            genrename = i['name']
            generobj, s = Genre.objects.get_or_create(name=genrename)
            book_id.genre.add(generobj)
            print(generobj)
        return book_id
