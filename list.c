#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;
}SList;

int SList_Create(SList **p/**out*/) {
    int data = 0;
    int ret = 0;
    SList *pHead = NULL;
    SList *node = NULL;
    SList *tmp = NULL;
    pHead = (SList *)malloc(sizeof(SList));
    if(pHead == NULL) {
        ret = -1;
        printf("SList_Create erro\n");
        goto End;
    }
    tmp = pHead;
    printf("请输入一个整数数据\n");
    scanf("%d", &data);
    while(data != -1) {
        node = (SList *)malloc(sizeof(SList));
        if(node == NULL) {
            ret = -1;
            printf("SList_Create erro\n");
            goto End;
        }
        node->data = data;
        tmp->next = node;
        tmp = node;
        printf("请输入一个整数数据\n");
        scanf("%d", &data);
    }
    node->next = NULL;
    *p = pHead;
End:
    if(ret != 0) {
        if(pHead != NULL) {
            free(pHead);
            pHead = NULL;
        }
        if(node != NULL) {
            free(node);
            node = NULL;
        }
    }
    return ret;
}

void print_List(SList *pHead) {
    SList *pTmp;
    if(pHead == NULL || pHead->next == NULL) {
        printf("SList is NULL\n");
    }
    pTmp = pHead;
    while(pTmp->next) {
        printf("%d ", pTmp->next->data);
        pTmp = pTmp->next;
    }
}

int insert_List(SList *pHead/**in*/, int targetNum, int insertNum) {
    int ret = 0;
    SList *pPre = NULL;
    SList *pCur = NULL;
    SList *pNode = NULL;
    if(pHead == NULL || pHead->next == NULL) {
        ret = -1;
        printf("insert_List erro\n");
        return ret;
    }
    pCur = pHead->next;
    pPre = pHead;
    pNode = (SList *)malloc(sizeof(SList));
    if(pNode == NULL) {
        ret = -1;
        printf("insert_List erro\n");
        return ret;
    }
    pNode->data = insertNum;
    while(pCur) {
        if(pCur->data == targetNum) {
            break;
        }else {
            pPre = pCur;
            pCur = pCur->next;
        }
    }
    pNode->next = pCur;
    pPre->next = pNode;
    return ret;
}

int delete_List(SList *pHead, int deleteNum) {
    int ret = 0;
    SList *pPre = NULL;
    SList *pCur = NULL;
    if(pHead == NULL || pHead->next == NULL) {
        ret = -1;
        printf("delete_List erro\n");
        return ret;
    }
    pPre = pHead;
    pCur = pHead->next;
    while(pCur) {
        if(pCur->data == deleteNum) {
            break;
        }else {
            pPre = pCur;
            pCur = pCur->next;
        }
    }
    if(pCur == NULL) {
        ret = -2;
        printf("not exist this num");
        return ret;
    }
    pPre->next = pCur->next;
    pCur->next = NULL;
    if(pCur != NULL) {
        free(pCur);
    }
    return ret;
}

void destory_List(SList **p) {
    SList *pHead = NULL;
    SList *tmp = NULL;
    if(p == NULL || *p == NULL) {
        return;
    }
    pHead = *p;
    while(pHead) {
        tmp = pHead->next;
        if(pHead != NULL) {
            free(pHead);
        }
        pHead = tmp;
    }
    *p = NULL;
}

void reverse_List(SList *pHead) {
    SList *pPre = NULL;
    SList *pCur = NULL;
    SList *pTmp = NULL;
    if(pHead == NULL || pHead->next == NULL || pHead->next->next == NULL) {
        return;
    }
    pPre = pHead->next;
    pCur = pHead->next->next;
    while(pCur) {
        pTmp = pCur->next;
        pCur->next = pPre;
        pPre = pCur;
        pCur = pTmp;
    }
    pHead->next->next = NULL;
    pHead->next = pPre;
}

int main() {
    int ret = 0;
    SList *node1 = NULL;
    ret = SList_Create(&node1);
    if(ret) {
        printf("create list erro\n");
    }
    print_List(node1);
    printf("\n insert_List\n");
    insert_List(node1, 20, 19);
    print_List(node1);
    printf("\n delete_List\n");
    delete_List(node1, 19);
    print_List(node1);
    printf("\n reverse_List\n");
    reverse_List(node1);
    print_List(node1);
    printf("\n destory_List\n");
    destory_List(&node1);
    system("pause");
    return 0;
}
