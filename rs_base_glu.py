# -*- coding: utf-8 -*-
# txt�t�@�C���̏������݂Ɠǂݍ���
#
# �ϐ��� = open(�t�@�C����,���[�h)
# with�\���iwith �t�@�C���ǂݍ��� as �ϐ��j�Fclose��������Ȃ�
# for �ϐ� in �I�u�W�F�N�g:
#     ���s���鏈��
# �X���C�X���g��������������̎擾 [0:6]
#
# Create 2017/06/30
# update 2017/06/30
# Auther Katsumi.Oshiro

import csv                  # csv���W���[���̓ǂݍ��݁iCSV�t�@�C���̓ǂݏ����j
import glob                 # glob���W���[���̓ǂݍ��݁i�t�@�C�����̃p�^�[���}�b�`���O�j
import pandas as pd         # pandas���W���[���̓ǂݍ���

print('RS_Base���t����CSV�f�[�^�̎捞�iSTART�j')
# �����i����ID�A���N�����j��������
birth = {}
# ���҃}�X�^�[�iname.csv�j�̓ǂݍ���
with open('../data/name.csv', 'r')as f:
    reader = csv.reader(f)
    for row in reader:
#       print(row[0],row[1],row[2],row[3])
        birth.update({row[0]:row[3]})

# ����(birth)�F���N�����̌����e�X�g�i����ID:679�j
print('����ID:679�̐��N����->', birth["679"])

# �N��v�Z�e�X�g�i����ID:679�j
today = int(pd.to_datetime('today').strftime('%Y%m%d'))
birthday = int(pd.to_datetime(birth["679"]).strftime('%Y%m%d'))
print('����ID:697�̔N��->', int((today - birthday)/ 10000))

# �t�H���_���̌��t�����t�@�C�����̎擾�i���C���h�J�[�h���g�p�\�j
txt_file = glob.glob('../data/labo/*.txt')

# �������ʂ̏o��
# ���f�[�^�Flow[0]���N����,low[1]����ID,low[2]����,low[3]����,low[5]�������ږ�,low[6]����,low[10]���ʒl�j
with open("../data/labo/GLU-P.csv", "w") as f:
    for file_name in txt_file:
        with open(file_name, 'r')as f2:
            reader = csv.reader(f2)
            for low in reader:
                if low[5] == "GLU-P":
                    writer = csv.writer(f, lineterminator='\n')
                    listdata = []
                    listdata.append(low[1])
                    today = int(pd.to_datetime(low[0]).strftime('%Y%m%d'))
                    birthday = int(pd.to_datetime(birth[low[1]]).strftime('%Y%m%d'))
                    listdata.append(int((today - birthday)/ 10000))
                    if low[1] == "679":
                        listdata.append('')
                        listdata.append('')
                        listdata.append('')
                        listdata.append(low[10])
                    elif low[6] == "H":
                        listdata.append('')
                        listdata.append('')
                        listdata.append(low[10])
                    elif low[6] == "L":
                        listdata.append('')
                        listdata.append(low[10])
                    else:
                        listdata.append(low[10])
                    listdata.append('')
                    writer.writerow(listdata)

print('RS_Base���t����CSV�f�[�^�̎捞�iEND�j')
