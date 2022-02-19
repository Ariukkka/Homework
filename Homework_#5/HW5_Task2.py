import pygal
  
from pygal.style import Style
  
custom_style = Style( colors = ('#FF0000' , '#0000FF' ,
                                '#00FF00' , '#000000',
                                '#FFD700'))

worldmap =  pygal.maps.world.World(style 
                                   = custom_style)
  
worldmap.title = 'Улсуудын стратегийн бүсчлэл'
  
worldmap.add('"А бүс" Countries', 
             ['ec', 'ee', 'eg', 'eh',
              'er', 'es','et'])
  
worldmap.add('"B бүс" Countries', 
             ['fr', 'fi'])
  
worldmap.add('"C бүс" Countries', 
             ['pa', 'pe', 'pg', 'ph', 'pk', 
               'pl','pr', 'ps', 'pt', 'py'])
  
worldmap.render_to_file('abc.svg')
  
print("Success")