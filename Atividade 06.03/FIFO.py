from collections import deque

class FifoScheduler:
    # Inicializador ( Construtor da classe )
    def __init__(self):
        self.fila_processos = deque()
        
    def adicionar_processo(self, pid, tempo_exec):
        processo = (pid, tempo_exec)
        self.fila_processos.append(processo)
    
    def remover_processos(self):
        if self.fila_processos:
            return self.fila_processos.popleft()
        else:
            print("nenhum processo para remover.")
            return
        
        # Função que simula o comportamento do agendador FIFO
    def fifo_scheduling(self):
        tempo_atual = 0
        tempos_espera = {}
        tempos_retorno = {}    
        
        print('\nExecução dos processos (FIFO):\n')
        
        while self.fila_processos:
            pid, tempo_exec = self.remover_processos()
            
            tempos_espera[pid] = tempo_atual
            tempos_retorno[pid] = tempo_atual + tempo_exec
            
            print(f'Processo {pid} executando... (tempo: {tempo_atual} -> {tempo_atual + tempo_exec})')
            
            tempo_atual += tempo_exec
        
        print ('\nResumo do escalonamento:')
        print('PID | Tempo de Espera | Tempo de Retorno')
        for pid in tempos_espera:
            print(f'{pid:^3} | {tempos_espera[pid]:^15} | {tempos_retorno[pid]:^14}')
            
            
scheduler = FifoScheduler()
scheduler.adicionar_processo(1,5)
scheduler.adicionar_processo(2,1)
scheduler.adicionar_processo(3,23)
scheduler.adicionar_processo(4,7)
scheduler.adicionar_processo(5,5)
scheduler.adicionar_processo(6,5)
scheduler.adicionar_processo(7,98)
scheduler.adicionar_processo(8,8)

scheduler.fifo_scheduling()