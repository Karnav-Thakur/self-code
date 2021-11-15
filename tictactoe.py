async def tictactoe(self,ctx):
  win = False
  # winning_conditions = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
  board = [["⬜","⬜","⬜"],["⬜","⬜","⬜"],["⬜","⬜","⬜"]]
  choices = ["a1","a2","a3","b1","b2","b3","c1","c2","c3"]
  s = ""
  turn = random.randint(1,2)
  for row in board:
      s += "".join(row)+ "\n"

  embed = discord.Embed(title = f"TicTacToe with {self.client.user.name}",description = s,colour = discord.Color.random())
  msg = await ctx.send(embed = embed)

  player1 = ctx.author
  player2 = self.client.user
  def check(message):
      return message.author == ctx.message.author

  def wincheck():
      if board[0][0] == board[0][1] == board[0][2] == '❎' or  board[0][0] == board[0][1] == board[0][2] == '🟠' or board[1][0] == board[1][1] == board[1][2] == '❎' or  board[1][0] == board[1][1] == board[1][2] == '🟠' or board[2][0] == board[2][1] == board[2][2] == '❎' or  board[2][0] == board[2][1] == board[2][2] == '🟠' or board[0][0] == board[1][1] == board[2][2] == '❎' or board[0][0] == board[1][1] == board[2][2] == '🟠' or board[0][2] == board[1][1] == board[2][0] == '❎' or board[0][2] == board[1][1] == board[2][0] == '🟠' or board[0][0] == board[1][0] == board[2][0] == '❎' or  board[0][0] == board[1][0] == board[2][0] == '🟠'or board[0][1] == board[1][1] == board[2][1] == '❎' or  board[0][1] == board[1][1] == board[2][1] == '🟠' or board[0][2] == board[1][2] == board[2][2] == '❎' or  board[0][2] == board[1][2] == board[2][2] == '🟠' :
          return True
      else:
          return False

  while win is False:

      if turn ==1:
          # ctx.author turn
          await ctx.send(f"{player1.mention} it's your turn, message with the postion (a1 is the top left a2 is the top middle)")
          response = await self.client.wait_for('message', check = check)
          res = re.findall(r"[^\W\d_]+|\d+", response.content.lower())
          try:
              res[1]
          except IndexError:
              await ctx.send('This was a wrong input, I am stopping the game')

          for row in board:
              s = ""
              if response.content.lower() not in choices:
                  await ctx.send("You already placed here")

              if choices == []:
                  await ctx.send("It's a Tie")
                  return

              if res[0] == 'a':
                  board[0][int(res[1])-1] = '❎'
                  turn =2
                  # await ctx.send(board)
                  for bruh in board:
                      s += "".join(bruh)+"\n"
                  embed2 = discord.Embed(title = f"TicTacToe with {self.client.user.name}",description = s,colour = discord.Color.random())
                  await msg.edit(embed= embed2)
                  popping_element = ""
                  popping_element += "".join(res)
                  choices.remove(popping_element)
                  a = wincheck()
                  if a is True:
                      await ctx.send(f"{player1.mention} Won!!")
                      win = True
                      return
                  else:
                      pass
                  break
              elif res[0] == 'b':
                  board[1][int(res[1])-1] = '❎'
                  turn =2
                  for bruh in board:
                      s += "".join(bruh)+"\n"
                  # await ctx.send(board)
                  embed2 = discord.Embed(title = f"TicTacToe with {self.client.user.name}",description = s,colour = discord.Color.random())
                  await msg.edit(embed= embed2)
                  popping_element = ""
                  popping_element += "".join(res)
                  choices.remove(popping_element)
                  a = wincheck()
                  if a is True:
                      await ctx.send(f"{player1.mention} Won!!")
                      win = True
                      return
                  else:
                      pass
                  break
              elif res[0] == 'c':
                  board[2][int(res[1])-1] = '❎'
                  turn =2
                  for bruh in board:
                      s += "".join(bruh)+"\n"
                  # await ctx.send(board)
                  embed2 = discord.Embed(title = f"TicTacToe with {self.client.user.name}",description = s,colour = discord.Color.random())
                  await msg.edit(embed= embed2)
                  popping_element = ""
                  popping_element += "".join(res)
                  choices.remove(popping_element)
                  a = wincheck()
                  if a is True:
                      await ctx.send(f"{player1.mention} Won!!")
                      win = True
                      return
                  else:
                      pass
                  break

      elif turn ==2:
          # self.client.user turn
          await ctx.send(f"{player2.mention} is playing...")
          for row in board:
              s = ""
              choice = random.choice(choices)
              rem = re.findall(r"[^\W\d_]+|\d+", choice)
              if choice not in choices:
                  continue
              if choices == []:
                  await ctx.send("It's a Tie")
                  return
              if rem[0] == 'a':
                  popping_element = ""
                  board[0][int(rem[1])-1] = '🟠'
                  turn =1
                  popping_element += "".join(rem)
                  choices.remove(popping_element)
                  # await ctx.send(board)
                  for bruh in board:
                      s += "".join(bruh)+"\n"
                  embed2 = discord.Embed(title = f"TicTacToe with {self.client.user.name}",description = s,colour = discord.Color.random())
                  await msg.edit(embed= embed2)
                  a = wincheck()
                  if a is True:
                      await ctx.send(f"{player2.mention} Won!!")
                      win = True
                      return
                  else:
                      pass
                  break
              elif rem[0] == 'b':
                  board[1][int(rem[1])-1] = '🟠'
                  turn =1
                  popping_element = ""
                  popping_element += "".join(rem)
                  choices.remove(popping_element)
                  for bruh in board:
                      s += "".join(bruh)+"\n"
                  # await ctx.send(board)
                  embed2 = discord.Embed(title = f"TicTacToe with {self.client.user.name}",description = s,colour = discord.Color.random())
                  await msg.edit(embed= embed2)
                  a = wincheck()
                  if a is True:
                      await ctx.send(f"{player2.mention} Won!!")
                      win = True
                      return
                  else:
                      pass
                  break
              elif rem[0] == 'c':
                  board[2][int(rem[1])-1] = '🟠'
                  turn =1
                  popping_element = ""
                  popping_element += "".join(rem)
                  choices.remove(popping_element)
                  for bruh in board:
                      s += "".join(bruh)+"\n"
                  # await ctx.send(board)
                  embed2 = discord.Embed(title = f"TicTacToe with {self.client.user.name}",description = s,colour = discord.Color.random())
                  await msg.edit(embed= embed2)
                  a = wincheck()
                  if a is True:
                      await ctx.send(f"{player2.mention} Won!!")
                      win = True
                      return
                  else:
                      pass
                  break
