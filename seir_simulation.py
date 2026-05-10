import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

# =============================================================================
# CONFIGURAÇÕES E PARÂMETROS DO MODELO
# =============================================================================

# Tamanho da grade (N x N)
GRID_SIZE = 50
# Parâmetros Epidemiológicos
R0 = 2.5
T_INC = 5.0  # Tempo de incubação (dias)
T_INF = 10.0 # Tempo infeccioso (dias)
LETALIDADE = 0.02 # 2% de taxa de letalidade

# Probabilidades de transição por passo de tempo (dt = 1 dia)
# Beta derivado de R0: R0 = beta * T_INF => beta = R0 / T_INF
BETA = R0 / T_INF
SIGMA = 1.0 / T_INC  # Taxa de progressão de Exposto para Infectado
GAMMA = 1.0 / T_INF  # Taxa de recuperação/remoção

# Estados do Autômato Celular
SUSCETIVEL = 0
EXPOSTO = 1
INFECTADO = 2
REMOVIDO = 3
MORTO = 4

# Cores para visualização: Branco, Amarelo, Vermelho, Verde, Preto
COLORS = ['#eeeeee', '#f1c40f', '#e74c3c', '#2ecc71', '#2c3e50']
CMAP = ListedColormap(COLORS)

# =============================================================================
# INICIALIZAÇÃO
# =============================================================================

grid = np.full((GRID_SIZE, GRID_SIZE), SUSCETIVEL)

# Infectar um paciente zero no centro
grid[GRID_SIZE//2, GRID_SIZE//2] = INFECTADO

# Histórico para o gráfico final
history = {
    'S': [], 'E': [], 'I': [], 'R': [], 'D': []
}

def get_neighbors_infected(r, c, current_grid):
    """Conta vizinhos infectados (vizinhança de Moore - 8 células)"""
    count = 0
    for i in range(max(0, r-1), min(GRID_SIZE, r+2)):
        for j in range(max(0, c-1), min(GRID_SIZE, c+2)):
            if (i != r or j != c) and current_grid[i, j] == INFECTADO:
                count += 1
    return count

def update(frame, img, ax):
    global grid
    new_grid = grid.copy()
    
    counts = {'S': 0, 'E': 0, 'I': 0, 'R': 0, 'D': 0}
    
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            state = grid[r, c]
            
            if state == SUSCETIVEL:
                n_inf = get_neighbors_infected(r, c, grid)
                # Probabilidade de infecção baseada no número de vizinhos doentes
                prob_inf = 1 - (1 - BETA)**n_inf
                if np.random.rand() < prob_inf:
                    new_grid[r, c] = EXPOSTO
                counts['S'] += 1
                
            elif state == EXPOSTO:
                if np.random.rand() < SIGMA:
                    new_grid[r, c] = INFECTADO
                counts['E'] += 1
                
            elif state == INFECTADO:
                if np.random.rand() < GAMMA:
                    if np.random.rand() < LETALIDADE:
                        new_grid[r, c] = MORTO
                    else:
                        new_grid[r, c] = REMOVIDO
                counts['I'] += 1
                
            elif state == REMOVIDO:
                counts['R'] += 1
            elif state == MORTO:
                counts['D'] += 1

    grid = new_grid
    img.set_data(grid)
    
    # Atualizar histórico
    history['S'].append(counts['S'])
    history['E'].append(counts['E'])
    history['I'].append(counts['I'])
    history['R'].append(counts['R'])
    history['D'].append(counts['D'])
    
    ax.set_title(f"Dia {frame} | S:{counts['S']} E:{counts['E']} I:{counts['I']} R:{counts['R']} D:{counts['D']}")
    return [img]

# =============================================================================
# EXECUÇÃO DA ANIMAÇÃO
# =============================================================================

fig, ax = plt.subplots(figsize=(8, 8))
img = ax.imshow(grid, cmap=CMAP, vmin=0, vmax=4, interpolation='nearest')
plt.colorbar(img, ticks=[0, 1, 2, 3, 4], format=plt.FuncFormatter(lambda x, pos: ['S', 'E', 'I', 'R', 'D'][int(x)]))

ani = animation.FuncAnimation(fig, update, fargs=(img, ax), frames=150, interval=50, repeat=False)

# Para salvar a animação (opcional, requer ffmpeg ou imagemagick)
# ani.save('simulacao_seir.mp4', writer='ffmpeg')

plt.show()

# =============================================================================
# GRÁFICO FINAL DE EVOLUÇÃO
# =============================================================================

plt.figure(figsize=(10, 6))
plt.plot(history['S'], label='Suscetíveis', color='#eeeeee', lw=2, path_effects=[plt.matplotlib.patheffects.withStroke(linewidth=3, foreground='black')])
plt.plot(history['E'], label='Expostos', color='#f1c40f', lw=2)
plt.plot(history['I'], label='Infectados', color='#e74c3c', lw=2)
plt.plot(history['R'], label='Removidos', color='#2ecc71', lw=2)
plt.plot(history['D'], label='Mortos', color='#2c3e50', lw=2)
plt.xlabel('Dias')
plt.ylabel('População')
plt.title('Evolução Temporal dos Compartimentos SEIR')
plt.legend()
plt.grid(alpha=0.3)
plt.show()
