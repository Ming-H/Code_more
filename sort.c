1、冒泡排序
时间复杂度：最好T=O(N)，最坏T=O(N2)
void Buble_Sort(ElementType A[], int N)
{
	for(P=N-1; P>0; P--)
	{
		flag = 0;
		for(i=0; i<P; i++)
		{
			if(A[i]>A[i+1])
			{
				Swap(A[i], A[i+1]);
			}
		}
		if(falg ==0)
			break;
	}
}

2、插入排序
时间复杂度：最好T=O(N)，最坏T=O(N2)
void Insertion_Sort(ElementType A[], int N)
{
	for(P=1; P<N; P++)
	{
		Tmp = A[P];
		for(i=P; i>0 && A[i-1]>Tmp; i--)
			A[i] = A[i-1];
		A[i] = Tmp;
	}
}

3、快速排序
void Quict_Sort(ElementType A[], int Left, int Right)
{
	if(CUTOFF <= Right - Left)
	{
		Pivot = Median3(A, Left, Right);
		i = Left; j = Right - 1;
		for(;;)
		{
			while(A[++i] < Pivot) { }
			while(A[--j] > Pivot) { }
			if(i<j)
				Swap(&A[i], &A[j]);
			else
				break;
		}
		Swap(&A[i], &A[right-1]);
		Quict_Sort(A, Left, i-1);
		Quict_Sort(A, i+1, Right);
	}
	else
		Insertion_sort(A+Left, Right-Left+1)
}

4、归并排序
void Merge(ElementType A[], ElementType TmpA[], int L, int R, int RightEnd)
{
	LeftEnd = R- 1;
	Tmp = L;
	NumElements = RightEnd -L +1;
	while(L<=LeftEnd && R<= RightEnd)
	{
		if(A[L] <= A[R]) TmpA[Tmp++] = A[L++];
		else TmpA[Tmp++] = A[R++];
	}
	while(L<=LeftEnd)
		TmpA[Tmp++] = A[L++];
	while(R<=RightEnd)
		TmpA[Tmp++] = A[R++];
	for(i=0;i<NumElements; i++, RightEnd--)
		A[RightEnd] = TmpA[RightEnd];
}

5、二分查找
6、最大子列和问题
