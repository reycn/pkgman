from pkgman import include

include(["numpy", "pandas"])

print(
    pandas.DataFrame(),
    numpy.mean(
        [
            1,
            2,
            3,
        ]
    ),
)
