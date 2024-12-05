
library(ggplot2)

# Step 1: Ler o arquivo CSV
data <- read.csv("dados_de_irrigacao.csv")

# Step 2: Gera um resumo
water_summary <- aggregate(Water ~ Irrigation_time, data = data, sum)

# Step 3: Calculao o percentual para o gráfico de pizza
water_summary$fraction = water_summary$Water / sum(water_summary$Water)
water_summary$percentage = round(water_summary$fraction * 100, 1)

dev.new()  
# Step 4: Create the pie chart
p1 <- ggplot(water_summary, aes(x = "", y = fraction, fill = Irrigation_time)) +
  geom_bar(stat = "identity", width = 1) +
  coord_polar(theta = "y") + 
  labs(title = "Percentual de água utilizada por dia, em 5 dias") +
  theme_void() +
  theme(legend.title = element_blank()) +
  geom_text(aes(label = paste(percentage, "%")), 
            position = position_stack(vjust = 0.5))


print(p1)


dev.new()

# Step 5: Cria o gráfico de barras
p2 <- ggplot(water_summary, aes(x = Irrigation_time, y = Water, fill = Irrigation_time)) +
  geom_bar(stat = "identity") +
  labs(title = "Quantidade de litros utilizados, por dia", 
       x = "Data da Irrigação", y = "Quantidade de água (L)") +
  theme_minimal() +
  theme(legend.title = element_blank())


print(p2)