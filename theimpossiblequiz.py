import asycnio 

@client.command()
async def impossiblequiz(ctx):
  with open('./jsons/theimpossiblequiz.json',encoding='utf-8') as f:
      data = json.load(f)

  for index,i in enumerate(data):
      embed = discord.Embed(title='Impossible Quiz',colour=discord.Color.random())
      embed.add_field(name=f'Question No. {index+1}',value=i['question'])
      view = View()
      for index,opt in enumerate(i['options']):
          if index < 2:
              button = TheImpossibleQuiz(opt,ButtonStyle.blurple,i['options'],i['answer_index'],row=1)
              view.add_item(button)
          if index >= 2:
              button = TheImpossibleQuiz(opt,ButtonStyle.blurple,i['options'],i['answer_index'],row=2)
              view.add_item(button)
      await ctx.respond(embed=embed,view=view)

      try:
          som = await client.wait_for('interaction',check=lambda interaction:interaction.data['component_type'] == 2,timeout=10.0)
      except asyncio.TimeoutError:
          await ctx.respond("You didn't respond in time, you are disqualified")
          return

      if 'return' in i['options']:
          return   

      await asyncio.sleep(1)
    
   
 
class TheImpossibleQuiz(Button):
    def __init__(self,label,style,options:list,answer,row):
        super().__init__(style=style,label=label,row=row)
        self.answer = answer
        self.options = options
    
    async def callback(self, interaction: discord.Interaction):
        a = interaction.followup            

        if self.options.index(self.label) == int(self.answer):
            for item in self.view.children:
                item.disabled = True
            
            await interaction.response.edit_message(view=self.view)
            await a.send('Correct Answer Proceed to next question')

        else:
            self.options.append('return')
            for item in self.view.children:
                item.disabled = True
            await interaction.response.edit_message(view=self.view)
            await a.send('Wrong Choice you are disqualified')
