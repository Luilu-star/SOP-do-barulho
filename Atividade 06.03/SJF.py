class SJFScheduler:

    def __init__(self):
        self.armario_de_processos = []

    def add_processo(self, pid, tempo_exec):
        proce = (tempo_exec, pid)
        self.armario_de_processos.append(proce)
        self.armario_de_processos.sort()
    
    def remove_processo(self):
        if self.armario_de_processos:
            return self.armario_de_processos.pop(0)
        else:
            print("Sem processsos para a remoção")
            return
    
    def SJF_scheduling(self):

        tempo_atual = 0
        exec_processos = []

        print('\nExecução dos processos na ordem SJF:\n ')

        while self.armario_de_processos:
            proce = self.remove_processo()
            if proce:
                tempo_exec, pid = proce  

                tempos_espera = tempo_atual
                tempos_retorno = tempo_exec + tempo_atual

                exec_processos.append((pid, tempos_espera, tempos_retorno))

                print(f'PRocesso {pid} executando...  (tempo: {tempo_atual} -> {tempos_retorno})')
                tempo_atual += tempo_exec

        print("\nResumo do escalonamento: ")
        print("PID | Tempo de Espera | Tempo de Retorno")
        for pid, tempos_espera, tempos_retorno in exec_processos:
            print(f'{pid:^3} | {tempos_espera:^15} | {tempos_retorno:^17}')

scheduler = SJFScheduler()
scheduler.add_processo(1,5)
scheduler.add_processo(2,1)
scheduler.add_processo(3,23)
scheduler.add_processo(4,7)
scheduler.add_processo(5,5)
scheduler.add_processo(6,5)
scheduler.add_processo(7,98)
scheduler.add_processo(8,8)

scheduler.SJF_scheduling()

#lambda é uma função anônima que não necessita de função definida anteriormente e mais comumente utilizada para usos de vez única.