class Movie:
    def __init__(self,name,hero,heroin):
        self.name=name;
        self.hero=hero;
        self.heroin=heroin;
    
    def info(self):
        print('moive name:',self.name)
        print('hero name:',self.hero)
        print('heroin name:',self.heroin)
    
    def save_data(self):
        with open('E:\\shyam\\programing\\PYTHON\\OOPS\\5_movie_data.txt','a') as f:
            f.write('Movie name :'+self.name+'\n')
            f.write('Hero name :'+self.hero+'\n')
            f.write('Heroin name :'+self.heroin+'\n')
            f.write('\n')


movie_list=[]
while True:
    m=Movie(input('enter the movie name:'),input('enter hero name'),input('enter heroin name'))
    movie_list.append(m)
    print('Movie inserted succesfully')
    print('Do you want to add another movie')
    option=input('enter yes on no.')
    if(option.lower()=='no'):
        break

print()
print('Movie data')
for movie in movie_list:
    movie.info()
    movie.save_data()
    print()
