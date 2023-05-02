# Import the necessary libraries


# Define the public key as a point (x, y)
public_key = (4090578498942620245623851636804746979286948998724755897608472602665899401735377653723701967333316170840828074536572297283230775592949024159395225707333857)

# Define the values of generator_x, generator_y, and p
generator_x = 55066263022277343669578718895168534326250603453777594175500187360389116729240
generator_y = 32670510020758816978083085130507043184471273380659243275938904335757337482424
p = 1157920892373161954235709850086879078528375642790749043826051257560570605115945

def find_public_key_x_public_key_y_and_private_key(public_key, generator_x, generator_y, p):
  # Initialize the result point (result_x, result_y) to the point at infinity (0, 0)
  result_x, result_y = 0, 0

  # Initialize the scalar value private_key to 0
  private_key_min = 1157920892373161954235
  private_key = private_key_min

  counter = 0

  # Perform scalar multiplication using the binary representation of T
  while (result_x, result_y) != public_key:
    # Double the result point (result_x, result_y)
    result_x, result_y = (result_x * 2) % p, (result_y * 2) % p

    # Increment the scalar value private_key
    private_key += 1

    
    # Increment the counter
    counter += 1

    print("Counter:", counter)
    

    # If the result point equals public_key, return the values of x, y, and private_key
    if (result_x, result_y) == public_key:
      return result_x, result_y, private_key

    # Add the generator point (generator_x, generator_y) to the result point (result_x, result_y)
    result_x, result_y = (result_x + generator_x) % p, (result_y + generator_y) % p

# Find x, y, and private_key using the public key
public_key_x, public_key_y, private_key = find_public_key_x_public_key_y_and_private_key(public_key, generator_x, generator_y, p)

# Print the values of x, y, and private_key
print("x:", public_key_x)
print("y:", public_key_y)
print("T:", private_key)



