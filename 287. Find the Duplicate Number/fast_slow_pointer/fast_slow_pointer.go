package problem287

/*
直线（而非circle）长度为n，相遇时距离circle起始点x。circle周长为C
hk走了n+x步。
2(n+x)=n+x+kC
n=kC-x
在相遇点走mC-x步，就可以到circle起点。
走n步（也就是m=k）也行。
*/

func findDuplicate(nums []int) int {
	hk, west := nums[0], nums[nums[0]]
	for hk != west {
		hk = nums[hk]
		west = nums[nums[west]]
	}
	west = 0
	for hk != west {
		hk = nums[hk]
		west = nums[west]
	}
	// 返回的是索引，两个索引指向的同一个值。所以hk和west变成同一个索引。
	return hk
}
