import numpy as np

class Talam:
    def dhruva_talam(self):
        dhruva_tala = [1, 0, 1, 1]
        dhruva=[]
        for i in range(3,10):  #for i in [3,4,5,7,9]: 
            dhruva_tala[0],dhruva_tala[2],dhruva_tala[3] = i, i, i
            dhruva_tala[1]=2
            Total = sum(dhruva_tala)
            dhruva.append(Total)
        Tot_dhruva = np.array(dhruva)
        remove_idx = [3,5]
        Tot_dhruva = np.delete(Tot_dhruva, remove_idx)
        print(Tot_dhruva)

    def matya_talam(self):
        matya_tala = [1, 0, 1]
        matya=[]
        for i in range(3,10):   
            matya_tala[0],matya_tala[2] = i, i
            matya_tala[1]=2
            Total = sum(matya_tala)
            matya.append(Total)
        Tot_matya = np.array(matya)
        remove_idx = [3,5]
        Tot_matya = np.delete(Tot_matya, remove_idx)
        print(Tot_matya)

    def roopaga_talam(self):
        roopaga_tala = [0, 1]
        roopaga=[]
        for i in range(3,10):   
            roopaga_tala[1] = i
            roopaga_tala[0]=2
            Total = sum(roopaga_tala)
            roopaga.append(Total)
        Tot_roopaga = np.array(roopaga)
        remove_idx = [3,5]
        Tot_roopaga = np.delete(Tot_roopaga, remove_idx)
        print(Tot_roopaga)
        

    def jambai_talam(self):
        jambai_tala = [ 1 , '-' , 0]
        jambai=[]
        for i in range(3,10):
            jambai_tala[0]= i
            jambai_tala[1], jambai_tala[2] = 1, 2
            Total = sum(jambai_tala)
            jambai.append(Total)
        Tot_jambai = np.array(jambai)
        remove_idx= [3,5]
        Tot_jambai = np.delete(Tot_jambai, remove_idx)
        print(Tot_jambai)

    def tiripuda_talam(self):
        tiripuda_tala = [1, 0, 0]
        tiripuda=[]
        for i in range(3,10):
            tiripuda_tala[0]= i
            tiripuda_tala[1], tiripuda_tala[2] = 2, 2
            Total = sum(tiripuda_tala)
            tiripuda.append(Total)
        Tot_tiripuda = np.array(tiripuda)
        remove_idx= [3,5]
        Tot_tiripuda = np.delete(Tot_tiripuda, remove_idx)
        print(Tot_tiripuda)

    def ada_talam(self):
        ada_tala = [ 1, 1, 0, 0]
        ada = []
        for i in range(3,10):
            ada_tala[0], ada_tala[1]= i, i
            ada_tala[2], ada_tala[3] = 2, 2
            Total = sum(ada_tala)
            ada.append(Total)
        Tot_ada = np.array(ada)
        remove_idx= [3,5]
        Tot_ada = np.delete(Tot_ada, remove_idx)
        print(Tot_ada)

    def eka_talam(self):
        eka_tala = [1]
        eka = []
        for i in range(3,10):
            eka_tala[0]= i
            Total = sum(eka_tala)
            eka.append(Total)
        Tot_eka = np.array(eka)
        remove_idx= [3,5]
        Tot_eka = np.delete(Tot_eka, remove_idx)
        print(Tot_eka)

T=Talam()
T.dhruva_talam()
T.matya_talam()
T.roopaga_talam()
T.jambai_talam()
T.tiripuda_talam()
T.ada_talam()
T.eka_talam()
    

    