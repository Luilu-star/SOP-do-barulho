class RRobinScheduler:
    def __init__(self, quantum):
        self.armario_de_processos = []
        self.quantum = quantum

    def add_proce(self, pid, tempo_exec):
        self.armario_de_processos.append((pid, tempo_exec))

    def RRobin_scheduling(self):
        tempo_atual = 0
        tempos_espera = {}
        tempos_retorno = {}
        execucoes = {}
        processos_restantes = self.armario_de_processos.copy()
        
        for pid, _ in processos_restantes:
            tempos_espera[pid] = 0
            execucoes[pid] = 0

        print(f"\nExecução dos processos na ordem Round Robin (Quantum: {self.quantum}):\n")
        
        while processos_restantes:
            pid, tempo_exec = processos_restantes.pop(0)
            execucoes[pid] += 1
            
            if tempo_exec > self.quantum:

                print(f"Processo {pid} executando... (Tempo: {tempo_atual} → {tempo_atual + self.quantum})")
                tempo_atual += self.quantum
                processos_restantes.append((pid, tempo_exec - self.quantum))

                for p_pid, _ in processos_restantes[:-1]:
                    if p_pid != pid:
                        tempos_espera[p_pid] += self.quantum
            else:
                print(f"Processo {pid} executando (Tempo: {tempo_atual} → {tempo_atual + tempo_exec})")
                print(f"Processo {pid} finalizou")
                tempo_atual += tempo_exec
                tempos_retorno[pid] = tempo_atual
                
                for p_pid, _ in processos_restantes:
                    tempos_espera[p_pid] += tempo_exec

        print("\nResumo do escalonamento:")
        print("PID | Tempo de Espera | Tempo de Retorno | Execuções")
        for pid in tempos_espera:
            print(f"{pid:^3} | {tempos_espera[pid]:^15} | {tempos_retorno[pid]:^16} | {execucoes[pid]:^10}")

rrobin_scheduler = RRobinScheduler(23)

rrobin_scheduler.add_proce(1, 125)
rrobin_scheduler.add_proce(2, 19)
rrobin_scheduler.add_proce(3, 23)
rrobin_scheduler.add_proce(4, 37)
rrobin_scheduler.add_proce(5, 245)
rrobin_scheduler.add_proce(6, 93)
rrobin_scheduler.add_proce(7, 98)
rrobin_scheduler.add_proce(8, 38)

rrobin_scheduler.RRobin_scheduling()