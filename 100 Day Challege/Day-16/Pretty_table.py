from prettytable import PrettyTable

table = PrettyTable()
table.title = "Pokeman details"
table.add_column("Pokemon Name", ["pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)
