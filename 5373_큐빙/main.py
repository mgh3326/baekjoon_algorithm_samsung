import sys

sys.stdin = open("./data/input.txt")
dir_point_list = [
    # 위
    {'L': [  # TODO 구현 다 못 함
        [0, 0],
        [0, 1],
        [0, 2],
    ],
        'F': [
            [0, 0],
            [0, 1],
            [0, 2],
        ],
        'R': [
            [0, 0],
            [0, 1],
            [0, 2],
        ],
        'D': [
            [0, 0],
            [0, 1],
            [0, 2],
        ], }
    ,

    {
        'L': [
            [2, 0],
            [2, 1],
            [2, 2],
        ],
        'D': [
            [2, 0],
            [2, 1],
            [2, 2],
        ],
        'R': [
            [2, 0],
            [2, 1],
            [2, 2],
        ],
        'F': [
            [2, 0],
            [2, 1],
            [2, 2],
        ], }
    ,
    # 앞 Front
    {
        'U': [
            [2, 0],
            [2, 1],
            [2, 2],
        ],
        'L': [
            [0, 2],
            [1, 2],
            [2, 2],
        ],
        'D': [
            [0, 2],
            [0, 1],
            [0, 0],
        ],
        'R': [
            [0, 0],
            [1, 0],
            [2, 0],
        ], }
    ,
    # back
    {
        'U': [
            [0, 0],
            [0, 1],
            [0, 2],
        ],
        'R': [
            [0, 2],
            [1, 2],
            [2, 2],
        ]
        ,
        'D': [
            [2, 2],
            [2, 1],
            [2, 0],
        ],
        'L': [
            [2, 0],
            [1, 0],
            [0, 0],
        ]
    }
    ,

    {
        'F': [
            [0, 0],
            [1, 0],
            [2, 0],
        ],
        'U': [
            [0, 0],
            [1, 0],
            [2, 0],
        ],
        'B': [
            [0, 0],
            [1, 0],
            [2, 0],
        ],
        'D': [
            [0, 0],
            [1, 0],
            [2, 0],
        ],
    }

    ,

    {

        'F': [
            [0, 2],
            [1, 2],
            [2, 2],
        ],
        'D': [
            [0, 2],
            [1, 2],
            [2, 2],
        ],
        'B': [
            [0, 2],
            [1, 2],
            [2, 2],
        ],
        'U': [
            [0, 2],
            [1, 2],
            [2, 2],
        ],
    }
    ,
]
dir_cube_list = [
    [
        [
            'L', 'F', 'R', 'D'
        ],
        [
            'L', 'D', 'R', 'F'
        ],
    ],
    [
        [
            'L', 'D', 'R', 'F'
        ],
        [
            'L', 'F', 'R', 'D'
        ],
    ],
    [  # Front
        [
            'U', 'L', 'D', 'R'
        ],
        [
            'U', 'R', 'D', 'L'
        ],
    ],
    [  # back
        [
            'U', 'R', 'D', 'L'
        ],
        [
            'U', 'L', 'D', 'R'
        ],
    ],
    [
        [
            'F', 'U', 'B', 'D'
        ],
        [
            'F', 'D', 'B', 'U'
        ],
    ],
    [
        [
            'F', 'D', 'B', 'U'
        ],
        [

            'F', 'U', 'B', 'D'
        ],

    ],

]
rotate_index_dict = {
    '+': 0,
    '-': 1,
}
cube_index_list = ['U', 'D', 'F', 'B', 'L', 'R']
cube_index_dict = {
    'U': 0,
    'D': 1,
    'F': 2,
    'B': 3,
    'L': 4,
    'R': 5,
}

n = int(input())
for _ in range(n):
    cube_list = [[['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w'], ],
                 [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y'], ],
                 [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r'], ],
                 [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o'], ],
                 [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g'], ],
                 [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b'], ], ]
    m_len = int(input())
    m_list = input().split()
    for cube_letter, rotate_dir in m_list:
        dir_ = dir_cube_list[cube_index_dict[cube_letter]][rotate_index_dict[rotate_dir]]
        point_list = dir_point_list[cube_index_dict[cube_letter]]
        first = [cube_list[cube_index_dict[dir_[0]]][point_list[dir_[0]][0][0]][point_list[dir_[0]][0][1]],
                 cube_list[cube_index_dict[dir_[0]]][point_list[dir_[0]][1][0]][point_list[dir_[0]][1][1]],
                 cube_list[cube_index_dict[dir_[0]]][point_list[dir_[0]][2][0]][point_list[dir_[0]][2][1]]]
        for i in range(len(dir_) - 1):
            for depth in range(3):
                cube_list[cube_index_dict[dir_[i]]][point_list[dir_[i]][depth][0]][point_list[dir_[i]][depth][1]] = \
                    cube_list[cube_index_dict[dir_[i + 1]]][point_list[dir_[i + 1]][depth][0]][
                        point_list[dir_[i + 1]][depth][1]]
        for depth in range(3):
            cube_list[cube_index_dict[dir_[-1]]][point_list[dir_[-1]][depth][0]][point_list[dir_[-1]][depth][1]] = \
                first[depth]
    for value in cube_list[0]:
        print(str.join("", value))
